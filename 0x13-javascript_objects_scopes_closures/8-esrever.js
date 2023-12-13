#!/usr/bin/node

exports.esrever = function (list){
  let count = 0;
  for (let y of list) {
     count = y ? count + 1 : count;;
  }
  let tmp = 0;
  for (let i = 0; i < count - 1; i++){
    for (let j = i + 1; j < count; j++) {
      if ( list[i] < list[j]) {
       	tmp = list[i];
	list[i] = list[j];
	list[j] = tmp;      
      }
    }
  }
  return (list);	
};
