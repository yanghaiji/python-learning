import test_package

test_package.send_message.send("hhhh")
test_package.send_message.send2("hhhh")


txt = test_package.receive_message.receive()
print(txt)
