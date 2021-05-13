#RicardoCaster_Matala3

def read_file(file):
    #file = open("C:/Users/User/OneDrive/Shana C semester B/Mavo_Lehandassat_YedaVenetunim/Matala3_Ricardo/fileMatala3_NoyaBirthday.txt", "r", encoding="utf-8")
    file_read = file.read()
    file_lines = file_read.split('\n')
    return file_lines


file = open("C:/Users/User/OneDrive/Shana C semester B/Mavo_Lehandassat_YedaVenetunim/Matala3_Ricardo/fileMatala3_NoyaBirthday.txt", "r", encoding="utf-8")
#print(read_file(file))
#read_file(file)

def messages_info(messagesFile):   
    list_of_contacts = []
    list_of_text = []
    list_of_datetimes = []
    
    file_lines = read_file(messagesFile)
    #print(file_lines)
    for line in file_lines:
        from_index = line.find("-") + 2
        first_twopoints = line.find(":")
        second_twopoints =  line[(first_twopoints+1):].find(":") 
        to_index = first_twopoints + second_twopoints + 1
        
        if from_index != -1 and second_twopoints != -1:
            list_of_contacts.append(line[from_index:to_index])
            list_of_datetimes.append(line[0:from_index-3])
            list_of_text.append(line[to_index+2:])
    
    #for datetime in list_of_datetimes:
    #    print(datetime)
    #print()
    #for cont in list_of_contacts:
    #    print(cont)
    #print()
    #for text in list_of_text:
    #    print(text)

    #print("^^^^^^^^")
    
    contacts = dict()
    id = 1
    for name in list_of_contacts :
        if name not in contacts:
            contacts[name] = id
            id+=1
        
    #print(contacts)
    #for i in contacts:
    #    print(i, contacts[i])
    
    list_of_messages = []
    dict_of_messages = dict()
    
    index = 0
    for hodaot in list_of_text:
        dict_of_messages = dict()
        dict_of_messages["datetime"] = list_of_datetimes[index]
        id = 0
        message_sender = list_of_contacts[index]
        for senders in contacts:
            if message_sender == senders:
                id = contacts[senders]
        dict_of_messages["id"] = id
        dict_of_messages["text"] = list_of_text[index]
        list_of_messages.append(dict_of_messages)
        index+=1
    #z=1
    #for n in list_of_messages:
    #    print(z)
    #   print(n)
    #    z+=1
    return list_of_messages
    #return "hi"
print(messages_info(file))
    
print()

def metadata_dictionary(whatsappGroup_Messages):
    
    file_lines = read_file(whatsappGroup_Messages)
    metadata_dict = dict()
    for line in file_lines:
        #print(line)
        if -1 != line.find("הקבוצה") and -1!= line.find("נוצרה על ידי"):
            index_before_groupname = 8 + line.find("הקבוצה") 
            index_after_groupname = -2 + line.find("נוצרה על ידי")
           
            metadata_dict["chat_name"] = line[index_before_groupname:index_after_groupname]
            metadata_dict["creation_date"] = line[:(index_before_groupname-8)]
            metadata_dict["creator"] = line[(index_after_groupname+12):]
    
    file = open("C:/Users/User/OneDrive/Shana C semester B/Mavo_Lehandassat_YedaVenetunim/Matala3_Ricardo/fileMatala3_NoyaBirthday.txt", "r", encoding="utf-8")
    ids = []        
    for lines in messages_info(file):
        ids.append(lines["id"])        
    num_of_participants = max(ids)
    metadata_dict["num_of_participants"] = num_of_participants    
            
    return metadata_dict
    
file = open("C:/Users/User/OneDrive/Shana C semester B/Mavo_Lehandassat_YedaVenetunim/Matala3_Ricardo/fileMatala3_NoyaBirthday.txt", "r", encoding="utf-8")
print(metadata_dictionary(file))

print()
file = open("C:/Users/User/OneDrive/Shana C semester B/Mavo_Lehandassat_YedaVenetunim/Matala3_Ricardo/fileMatala3_NoyaBirthday.txt", "r", encoding="utf-8")
def shlav_revii(file):
    shlav2and3_dict = dict()
    shlav2and3_dict["messages"] = messages_info(file)
    file = open("C:/Users/User/OneDrive/Shana C semester B/Mavo_Lehandassat_YedaVenetunim/Matala3_Ricardo/fileMatala3_NoyaBirthday.txt", "r", encoding="utf-8")
    shlav2and3_dict["metadata"] = metadata_dictionary(file)
    
    return shlav2and3_dict

print(shlav_revii(file))
print("****")
import json
def transfering_to_json():
    file = open("C:/Users/User/OneDrive/Shana C semester B/Mavo_Lehandassat_YedaVenetunim/Matala3_Ricardo/fileMatala3_NoyaBirthday.txt", "r", encoding="utf-8")
    return json.dumps(shlav_revii(file), ensure_ascii=False, indent=6)

print(transfering_to_json())
print()
print()
print(" ----------------  -----------  -------------")
chat_name = "יום הולדת בנות לנוי'ה" + ".txt"
file = open(chat_name, "w", encoding = " utf8")
messages_file = open("C:/Users/User/OneDrive/Shana C semester B/Mavo_Lehandassat_YedaVenetunim/Matala3_Ricardo/fileMatala3_NoyaBirthday.txt", "r", encoding="utf-8")

json.dump(shlav_revii(messages_file),file, ensure_ascii=False,indent=6)

file.close()
file = open(chat_name, "r", encoding=" utf8")
print(json.load(file))
file.close()

