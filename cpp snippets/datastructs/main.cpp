#include <iostream>

/*
        Prepend addNode structure, added values to the back of the list so printing was backwards.
        Node* add = new Node(val);
        add->nxt = this->head;
        this->head = add;
*/
class Node {
public:
    int val = 0;
    Node* nxt;
    Node(int value) {
        this->val = value;
        this->nxt = nullptr;
    }
};

class LinkedList {
    public:
    Node* head;
    LinkedList(){
        this->head = nullptr;
    }
    void addNode(int val){
        Node* vol = new Node(val);
        vol->nxt = nullptr;
        //If the head of the list is empty (i.e list is empty)
        if (this->head == nullptr){
            this->head = vol;
            return;
        }
        //Find the current head of the list and append the new object to the front.
        Node* current = this->head;
        while (current->nxt != nullptr){
            current = current->nxt;
        }
        current->nxt = vol;
    }
    void printList(){
        Node* current = head;
        while(current != nullptr){
            std::cout << current->val << std::endl;
            current = current->nxt;
        }
    }
};

int main(){

    LinkedList o = LinkedList();
    o.addNode(10);
    o.addNode(20);
    o.addNode(30);
    o.printList();

    return 0;
}