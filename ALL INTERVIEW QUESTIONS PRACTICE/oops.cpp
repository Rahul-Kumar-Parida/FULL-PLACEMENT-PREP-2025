#include<iostream>
using namespace std;

/*
//classes & Objects
class Student{  //class
    public:
        string name;
        int age;
        int rollno;
    private:
        void show(){
            cout<<"I am Student Class!";
        }
};

int main(){
    Student s1;  //object 1
    s1.name="Rahul";
    s1.age=22;
    s1.rollno=23240025;

    cout<<s1.name<< " "<<s1.age<<" "<<s1.rollno<<endl;
    // s1.show(); //can not access because its member function is private
    return 0;
}

*/


//Encapsulation
class BankAccount{
    private:
        double balance;
    public:

        BankAccount(){
            balance=0.0;
        }

        void Deposit(double amount){
            if(amount>0){
                balance+=amount;
                cout<<"Diposited"<<endl;
            }else{
                cout<<"Invalid Diposited!!"<<endl;
            }
        }

        void Withdraw(double amount){
            if(amount>0 && amount<=balance){
                balance-=amount;
                cout<<"Withdral Successful"<<endl;
            }else{
                cout<<"Invalid Amount"<<endl;
            }
        }

        void get_balance(){
            cout<<"Current Balance: " <<balance<<endl;
        }
};

int main(){
    BankAccount P1;
    P1.Deposit(1000);
    P1.Withdraw(500);
    P1.get_balance();
    return 0;
}








