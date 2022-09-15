
#Con un modelo llamado m, utilizar estas funciones
#para imprimir todas sus variables:

print("------------------")
print("Funcion Objetivo: ",str(round(m.ObjVal,2)))
print("------------------")

#Archivo con valores de variables
nvariables = 0
f = open("variables.txt","w")
for var in m.getVars():
    f.write(str(var) + "     " + str(var.getAttr("X")) + "\n")
    nvariables += 1
f.close()

#Variables con valor
f = open("variables_valor.txt","w")
for var in m.getVars():
    if var.getAttr("X"):
        f.write(str(var) + "     " + str(var.getAttr("X")) + "\n")
f.close()

print("------------------")
print(f"Numero de Variables: {nvariables}")
print("------------------")

#Archivo con valores de holgura Restricciones
nrestricciones = 0
f = open("restricciones.txt","w")
for constr in m.getConstrs():
    f.write(str(constr.index) + ":       " + str(constr) + " " + str(constr.getAttr("slack")) + "\n")
    nrestricciones += 1
f.close()

#Holguras con valor
f = open("restricciones_con_holgura.txt","w")
for constr in m.getConstrs():
    if constr.getAttr("slack"):
        f.write(str(constr) + " " + str(constr.getAttr("slack")) + "\n")
f.close()

print("------------------")
print(f"Numero de Restricciones: {nrestricciones}")
print("------------------")

