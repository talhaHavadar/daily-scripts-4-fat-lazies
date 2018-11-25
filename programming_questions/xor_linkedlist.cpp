#include <iostream>
using namespace std;

class XORNode {
	public:
		int value;
		long int both;
		
		XORNode(int value) {
			this->value = value;
			this->both = 0;
		};

		void add(XORNode* pNode) {
			if (this->both == 0) {
				this->both ^= (long int) pNode;	
				pNode->both = 0 ^ (long int)this; 
			} else {
				XORNode* pNext = (XORNode*)(this->both ^ 0);
				XORNode* pPrev = this;
				while (pNext->both ^ (long int)pPrev) {
					pPrev = pNext;
					pNext = (XORNode*) (pNext->both ^ (long int)pPrev);
				}
				pNode->both = (long int) pNext ^ 0;
				pNext->both = (long int) pPrev ^ (long int) pNode;
			}
		};
		
		XORNode* get(int index) {
			if (index == 0) {
				return this;
			}
			
			XORNode* pCurrent = (XORNode*)(this->both ^ 0);
			if (index == 1) {
				return pCurrent;
			}
			
			int count = 1;
			XORNode* pPrev = this;
			while(count != index) {
				long int xorResult = ((long int)pPrev ^ pCurrent->both);
				if (xorResult == 0) {
					return NULL;
				}
				XORNode* temp = (XORNode*) xorResult;
				pPrev = pCurrent;
				pCurrent = temp;
				count++;
			}
			return pCurrent;
		}
	
};


int main() {
	// your code goes here
	XORNode first(5);
	XORNode second(4);
	XORNode third(3);
	
	first.add(&second);
	first.add(&third);
	
	cout << first.get(2)->value;
	
	return 0;
}
