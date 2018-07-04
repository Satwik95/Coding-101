#include<iostream>
#include<unordered_map>

using namespace std;

#define hashmap unordered_map<char,node*>

 class node{
 public:
 	char data;
 	hashmap h;
 	bool isTerminal;

 	node(char d){
 		data = d;
 		isTerminal = false;
 	}
 };

 class Trie{
 	 node* root;
 public:
 	Trie(){
 		root = new node('\0');
 	}

 	//Insertion
 	void addWord(char* word){
 		node* temp = root;
 		for(int i=0;word[i]!='\0';i++){
 			char ch = word[i];
 			if (temp->h.count(ch)==0){
 				node* child = new node(ch);
 				temp->h[ch] = child; //its basically temp->next = child
 				temp = child;
 	
 			else{
 				temp = temp->h[ch];
 			}
 			temp->isTerminal = true;
 		}
 	}

 	bool search(char* word){
 		node* temp = root;
 		for(int i=0;word[i]!='\0';i++){
 			char ch = word[i];
 			if(temp->h.count(ch)!=0){
 				temp=temp->h[ch];
 			}
 			else{
 				return false;
 			}
 		}
 		return temp->isTerminal;
 	}

 }; 

 int main()
 {
 	Trie t;
 	char word[10][100] = {"apple","ape","coder","satwik"};

 	for(int i=0;i<5;i++){
 		t.addWord(word[i]);
 	}

 	char searchword[100]
; 	cin.getline(searchword,100);

 	if(t.search(searchword)){
 		cout<<searchword<<" found"<<endl;
 	}
 	else{
 		cout<<searchword<<" not found"<<endl;
 	}

 	return 0;
 }