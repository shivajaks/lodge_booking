from django.shortcuts import render
def showform(request):
    return render(request,"index.html")
def save(request):
    name=request.POST.get("t1")
    con=request.POST.get("t2")
    add=request.POST.get("t3")
    room=int(request.POST.get("t4"))
    f1=(request.POST.get("t5"))
    f2=(request.POST.get("t6"))
    f3=(request.POST.get("t7"))
    if f1==None:
        f1=0
    if f2==None:
        f2=0
    if f3==None:
        f3=0
    list1=[int(f1),int(f2),int(f3)]
    bill=room+sum(list1)
    return render(request,"index.html",{"data":bill})
