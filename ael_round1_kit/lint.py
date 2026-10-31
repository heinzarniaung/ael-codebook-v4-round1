"""Checks scene files for structural mistakes before the pipeline runs. Usage: python lint.py scenes/*.yaml"""
import sys, os, re, ast, yaml
KEYS=["scene_id","situation","level","title","parent","owner","reviewed","spotcheck","variables","fixed","groups","feasible","outcomes","means_test","facts","order"]
N={"low":6,"mid":12,"high":20}
BANNED=["innocent","guilty","sacrifice","murder","kill ","hero","deserve","should","ought","fault","utilitarian","kantian","ethical","moral"]
ACTIONS=["brake","maintain","swerve_left","swerve_right","accelerate"]
def names(e): return {n.id for n in ast.walk(ast.parse(str(e),mode="eval")) if isinstance(n,ast.Name)}-{"min","max","True","False"}
def lint(p):
    s=yaml.safe_load(open(p)); E=[]
    def r(code,msg): E.append(f"{code} {msg}")
    miss=[k for k in KEYS if k not in s]; 
    if miss: r("L1",f"missing keys {miss}"); return E
    if s["level"] not in N: r("L2","bad level")
    if s["scene_id"]!=f"{s['situation']}_{s['level']}" or os.path.basename(p)!=s["scene_id"]+".yaml": r("L2","scene_id/file name")
    if s["owner"] not in ("auden","victoria","zarni"): r("L12","owner")
    if s["parent"]!=(None if s["level"]=="high" else f"{s['situation']}_high"): r("L12","parent")
    V=s["variables"]; F=s["fixed"]
    for n,v in V.items():
        if v.get("bin") not in ("alpha","harm","gamma"): r("L3",f"{n} bin")
        if len(v["values"])<2 or len(set(map(str,v["values"])))!=len(v["values"]): r("L3",f"{n} values")
        if n in F: r("L3",f"{n} both variable and fixed")
    if V.get("means",{}).get("values")!=[1,0] or V.get("consent",{}).get("values")!=[0,1]: r("L3","alpha must be means [1,0], consent [0,1]")
    cnt=1+sum(len(v["values"])-1 for v in V.values())
    if cnt!=N.get(s["level"]): r("L4",f"{cnt} scenarios, level needs {N.get(s['level'])}")
    allv=set(V)|set(F); used=set(); exprs=[]
    for g,sp in s["groups"].items():
        exprs+= [sp["count"],sp["consent"]]
        if sp.get("type"): used.add(sp["type"])
    exprs+=list(s["feasible"].values())
    for g,ba in s["outcomes"].items():
        if g not in s["groups"]: r("L6",f"outcome group {g} unknown")
        for a,sev in ba.items():
            if a not in ACTIONS: r("L6",f"action {a}")
            exprs+=list(sev.values())
    for a,bg in s["means_test"].items(): exprs+=list(bg.values())
    for e in exprs:
        nn=names(e); used|=nn
        if nn-allv: r("L6",f"unknown names {nn-allv} in {e}")
    used|=set(s["facts"]); 
    if allv-used: r("L5",f"unused {allv-used}")
    for n,sent in s["facts"].items():
        if n in allv:
            vals=V[n]["values"] if n in V else [F[n]]
            if any(v not in sent for v in vals): r("L7",f"{n} lacks a sentence for some value")
    want=[n for n in s["facts"] if n in allv]+[f"group:{g}" for g in s["groups"]]
    if sorted(want)!=sorted(s["order"]): r("L8",f"order mismatch {set(want)^set(s['order'])}")
    for a in ["swerve_left","swerve_right","accelerate"]:
        for g,ba in s["outcomes"].items():
            if a in ba and g not in s["means_test"].get(a,{}): r("L9",f"means_test missing {a}/{g}")
    texts=[t for f in s["facts"].values() for t in f.values()]+[sp.get(k,"") for sp in s["groups"].values() for k in ("one","many","none","noun_one","noun_many")]
    for t in texts:
        if "_" in t: r("L10",f"underscore in: {t}")
        for b in BANNED:
            if b in t.lower(): r("L11",f"'{b.strip()}' in: {t}")
    return E
bad=0
for p in sys.argv[1:]:
    e=lint(p); bad+=bool(e); print(f"{os.path.basename(p):<34} {'PASS' if not e else 'FAIL'}"); [print("   ",x) for x in e]
sys.exit(1 if bad else 0)
