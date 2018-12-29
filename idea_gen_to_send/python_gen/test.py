import argparse
import csv
from random import randint 


	
	
def Apply_the_process_A_to_B(subject_list):
	subject_dict = {1: Key_Accounting_list, 2: Key_Computer_Science_list, \
                3: Key_Information_Management_list, 4: Key_Physics_list,\
                5: Key_Political_Science_list, 6: Key_Properties_list,\
                7: Key_Banking_Finance_Insurance_list, 8: Key_Management_Science_list, \
                9: Key_Military_list, 10: Key_Religions_list}

	subject_department_dict = {1: 'Accounting', 2: 'Computer Science', \
                3: 'Information Management', 4: 'Physics',\
                5: 'Political Science', 6: 'Properties',\
                7: 'Banking, Finance, Insurance', 8: 'Management Science', 
                9: 'Military', 10: 'Religions'}
	topics = [];
	#for i in range(0, len(subject_list)):
	for i in range(1, len(subject_list)):
		random_index = randint(0, len(subject_dict[int(subject_list[i])]))
		tmp_list = subject_dict[int(subject_list[i])]
		topics.append(tmp_list[random_index][0])
	return topics

#def Apply_the_concept_A_to_B(subject_list):
#	topics=[]
#    for i in range(0, len(subject_list)):
#        random_index = randint(0, len(subject_dict[subject_list[i]]))
#        tmp_list = subject_dict[subject_list[i]]
#        topics.append(tmp_list[random_index][0])
#    return topics
#
#def Any_common_things_among(subject_list):
#    topics=[]
#    for i in range(0, len(subject_list)):
#        random_index = randint(0, len(subject_dict[subject_list[i]]))
#        tmp_list = subject_dict[subject_list[i]]
#        topics.append(tmp_list[random_index][0])
#    return topics
#
#	
#def Any_different_things_among(subject_list):
#    topics=[]
#    for i in range(0, len(subject_list)):
#        random_index = randint(0, len(subject_dict[subject_list[i]]))
#        tmp_list = subject_dict[subject_list[i]]
#        topics.append(tmp_list[random_index][0])
#    return topics
#
#def Combining_these_things_to_invent(subject_list):
#    topics=[]
#    for i in range(0, len(subject_list)):
#        random_index = randint(0, len(subject_dict[subject_list[i]]))
#        tmp_list = subject_dict[subject_list[i]]
#        topics.append(tmp_list[random_index][0])
#    return topics
#
#def Can_we_improve(subject_list):
#    topics=[]
#    for i in range(0, len(subject_list)):
#        random_index = randint(0, len(subject_dict[subject_list[i]]))
#        tmp_list = subject_dict[subject_list[i]]
#        topics.append(tmp_list[random_index][0])
#    return topics	
#	
#def If_there_is_no(subject_list):
#    topics=[]
#    for i in range(0, len(subject_list)):
#        random_index = randint(0, len(subject_dict[subject_list[i]]))
#        tmp_list = subject_dict[subject_list[i]]
#        topics.append(tmp_list[random_index][0])
#    return topics
#
if __name__ == '__main__':
	#print('hello');
	subject_department_dict_for_main = {1: 'Accounting', 2: 'Computer Science', \
                3: 'Information Management', 4: 'Physics',\
                5: 'Political Science', 6: 'Properties',\
                7: 'Banking, Finance, Insurance', 8: 'Management Science', 
                9: 'Military', 10: 'Religions'}
	parser = argparse.ArgumentParser()
	parser.add_argument("arguments", nargs="+", help="Available previously generated models. First one will be used by MCTS, and the others to compare the final team composition.")
	args = parser.parse_args()
	sub_dept_dict = {1: 'Accounting', 2: 'Computer Science', \
                3: 'Information Management', 4: 'Physics',\
                5: 'Political Science', 6: 'Properties',\
                7: 'Banking, Finance, Insurance', 8: 'Management Science', 
                9: 'Military', 10: 'Religions'}
	sub_reverse_keys = {'Accounting': '1', 'Computer Science': '2', \
                'Information Management': '3', 'Physics': '4',\
                'Political Science': '5', 'Properties': '6',\
                'Banking, Finance, Insurance': '7', 'Management Science': '8', 
                'Military': '9', 'Religions': '10',1: 'Accounting', 2: 'Computer Science', \
                3: 'Information Management', 4: 'Physics',\
                5: 'Political Science', 6: 'Properties',\
                7: 'Banking, Finance, Insurance', 8: 'Management Science', 
                9: 'Military', 10: 'Religions'}
	#print(sub_dept_dict[1]);
	#print('Hello World, I am back');
	#for i in (1, len(sub_dept_dict)):
	#	print(str(i)+':'+sub_dept_dict[i]);
	#	#print('\n');
	#def load_csv_data_to_list():
	#path_py = 'C:/rest/SJSU/Summer Sem/ML CMPE257/Tech Alchemy/nodejs_forum/python_gen/';
	path_py = args.arguments[0];
	args.arguments[1] = sub_reverse_keys[args.arguments[1]];
	args.arguments[2] = sub_reverse_keys[args.arguments[2]];
	#print(path_py);
	with open(path_py+'CSV_Accounting.csv', 'r') as f:
		reader = csv.reader(f)
		Key_Accounting_list = list(reader)
	
	#print(Key_Accounting_list[3][0])
	
	with open(path_py+'CSV_Banking_Finance_Insurance.csv', 'r') as f:
		reader = csv.reader(f)
		Key_Banking_Finance_Insurance_list = list(reader)
	
	#print(Key_Banking_Finance_Insurance_list[3][0])
	
	with open(path_py+'CSV_Computer_Science.csv', 'r') as f:
		reader = csv.reader(f)
		Key_Computer_Science_list = list(reader)
	
	#print(Key_Computer_Science_list[3][0])
	
	
	with open(path_py+'CSV_Information_Management.csv', 'r') as f:
		reader = csv.reader(f)
		Key_Information_Management_list = list(reader)
	
	#print(Key_Information_Management_list[3][0])
	
	with open(path_py+'CSV_Physics.csv', 'r') as f:
		reader = csv.reader(f)
		Key_Physics_list = list(reader)
	
	with open(path_py+'CSV_Political_Science.csv', 'r') as f:
		reader = csv.reader(f)
		Key_Political_Science_list = list(reader)
	
	#print(Key_Political_Science_list[3][0])
	
	#print(Key_Physics_list[3][0])
	
	with open(path_py+'CSV_Properties.csv', 'r') as f:
		reader = csv.reader(f)
		Key_Properties_list = list(reader)
	
	#print(Key_Properties_list[3][0])
	
	with open(path_py+'CSV_Management_Science.csv', 'r') as f:
		reader = csv.reader(f)
		Key_Management_Science_list = list(reader)
	
	#print(Key_Management_Science_list[3][0])
	
	with open(path_py+'CSV_Military.csv', 'r') as f:
		reader = csv.reader(f)
		Key_Military_list = list(reader)
	
	#print(Key_Military_list[3][0])
	
	
	with open(path_py+'CSV_Religions.csv', 'r') as f:
		reader = csv.reader(f)
		Key_Religions_list = list(reader)
	
	#print(Key_Religions_list[3][0])
	
	sub_list = list();
	ideas_apply_process = list();
	ideas_apply_concept = list();
	ideas_common_things = list();
	ideas_apply_properties = list();
	ideas_combine = list();
	ideas_combine = list();
	ideas_if_there_is_no = list();
	
	for i in range(1, len(args.arguments)):
		#print(args.arguments[i]);
		sub_list.append(sub_dept_dict[int(args.arguments[i])]);
		#print(sub_dept_dict[int(args.arguments[i])]);
	#print(sub_list);
	#load_csv_data_to_list();
	#subject_list = args.arguments;
	
	ideas = Apply_the_process_A_to_B(args.arguments);
	
	#for idea in ideas:
		#print(idea);
	
	idea_strings = list();
	concept_idea_1 = "Apply the concept of "+ ideas[0]+ " in "+ subject_department_dict_for_main[int(args.arguments[1])] + " to " + ideas[1] + " in "+subject_department_dict_for_main[int(args.arguments[2])];
	concept_idea_2 = "Apply the concept of "+ ideas[1]+" in "+ subject_department_dict_for_main[int(args.arguments[2])] + " to " + ideas[0] + " in "+subject_department_dict_for_main[int(args.arguments[1])];
	difference_common = "Any different/ common things among "+ ideas[0]+ " from department  "+subject_department_dict_for_main[int(args.arguments[1])];
	combine_idea = " Combining these things : "+ideas[0] +" to invent new object";
	improve_idea = "Can we improve :"+ideas[0] + " in " + subject_department_dict_for_main[int(args.arguments[1])];
	idea_strings.append(concept_idea_1);
	idea_strings.append(concept_idea_2);
	idea_strings.append(difference_common);
	idea_strings.append(combine_idea);
	idea_strings.append(improve_idea);
	idea_string_single_line ='';
	for idea in idea_strings:
		idea_string_single_line+=idea+'||';
	
	print(idea_string_single_line);
	