import json

encoded_str = json.dumps(dict(apple="cat", banana="dog"))


print(f"json obj: {encoded_str}")




"""
Flutter:

Map<String, dynamic> student_info = jsonDecode(bodyOfNoti);

print('Name, ${student_info['data']['name']}!');
print('ID, ${student_info["data"]["studentId"]}!');
print('School, ${student_info["data"]["school"]["name"]}!');
print('Class, ${student_info["data"]["clazz"]["name"]}!');

Then change: body = decode_server_response(server_error_code, received_string)

def decode_server_response(server_error_code, received_string):
	try:
		if (server_error_code == "00"):			
			# Return body of UI message	
			return received_string
		else:
			return None
	except:
		return None
		print("Error: Server response's format is incorrect !!!!!!!!!\n")


"""