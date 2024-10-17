class Stack{
    constructor(){
        this.stackArr=[];
        this.length=0;
    }

    push(value){
        this.length+=1;
        this.stackArr.push(value)
    }

    pop(){
        this.length-=1;
        return this.stackArr.pop()
    }

    front(){
        return this.stackArr[this.length-1]
    }
}

let our_first_stack = new Stack();
our_first_stack.push(6);
our_first_stack.push(5);
our_first_stack.push(4);
our_first_stack.push(3);
our_first_stack.push(2);
our_first_stack.push(0);

console.log(our_first_stack.pop());
console.log(our_first_stack.front());
console.log(our_first_stack.pop());
