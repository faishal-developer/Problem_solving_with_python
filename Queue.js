class Queue{
    constructor(){
        this.stackArr=[];
        this.length=0;
    }

    enqueue(value){
        this.length+=1;
        this.stackArr.push(value)
    }

    dequeue(){
        this.length-=1;
        return this.stackArr.shift();
    }

    front(){
        return this.stackArr[0]
    }
}

let our_first_queue = new Queue();
our_first_queue.enqueue(6);
our_first_queue.enqueue(5);
our_first_queue.enqueue(4);
our_first_queue.enqueue(3);
our_first_queue.enqueue(2);
our_first_queue.enqueue(0);

console.log(our_first_queue.dequeue());
console.log(our_first_queue.front());
console.log(our_first_queue.dequeue());
