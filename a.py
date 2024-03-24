# Print Welcome Message string files
message = "Hello World!"
print(message, len(message), message[5:])
print(message.lower())

message = message.replace("World", "Universe")
print(message.lower())

# m = "{}, {} Welcome to the jungle".format("Hello", "Manish")
m = f'{"manish"} hihihihihi {message.upper()}'
print(m)

print(help(str))
