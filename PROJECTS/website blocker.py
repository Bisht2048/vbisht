
website=["www.instagram.com"]
host_path="C:/Users/Vaibhav/Documents/host/hosts"
redirect="127.0.0.1"

# with open(host_path,"r+")as hostfile:
#     content=hostfile.readlines()
#     for i in website:
#         if i not in content:
#             # hostfile.seek(0)
#             with open(host_path, "a") as hostfile2:
#                 hostfile2.write(f"{redirect} {i}")

# delete
with open(host_path,"r+")as host2:
    content=host2.readlines()
    # host2.seek(0)
    for i in website:
        if i not in content:
            host2.write(f"\n {redirect} {i}")