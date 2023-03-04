import torchvision.models as models

net=models.mobilenet_v3_small(pretrained=True)

netlist=list(net.children())
print(len(netlist))
i = 0
for var in netlist:
    print(i,":",var)
    i=i+1
