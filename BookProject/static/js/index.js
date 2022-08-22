function readURL(input) {
    if (input.files && input.files[0]) {
      var reader = new FileReader();
      reader.onload = function(e) {
        document.getElementById('preview').src = e.target.result;
      };
      reader.readAsDataURL(input.files[0]);
    } else {
      document.getElementById('preview').src = "";
    }
}


// document.getElementById("btn").addEventListener("click",function(){
//   let bookname=document.getElementById("title").value;
//   console.log(bookname);
//   let button_make=document.createElement("button");
//   let bookname_node=document.createTextNode(bookname);
//   button_make.appendChild(bookname_node);
//   document.body.appendChild(button_make);

// })

document.getElementById("btn").addEventListener("click",function(){
  let bookname=document.getElementById("book_name").value;
  let writer=document.getElementById("writer").value;
  let sellprice=document.getElementById("sell_price").value;
  let originalprice=document.getElementById("original_price").value;

  let parent=document.querySelector('#sell');

  let div_ele=document.createElement("div");
  parent.insertBefore(div_ele,parent.firstChild);
  div_ele.setAttribute('id',"sell_box");  // 속성값 넣기 element.setAttribute("속성","속성값")

  parent=document.querySelector('#sell_box'); // 생성된 sell_box 안에 p 넣을거

  div_ele=document.createElement("div");
  parent.insertBefore(div_ele,null);
  div_ele.setAttribute('class',"card");

  parent=document.querySelector('.card'); // 생성된 sell_box 안에 p 넣을거

  let img_ele=document.createElement("img");
  parent.insertBefore(img_ele,null);
  img_ele.setAttribute('class',"card-img-top");
  img_ele.setAttribute('alt',"물건");

  div_ele=document.createElement("div");
  parent.insertBefore(div_ele,null);
  div_ele.setAttribute('class',"card-body");

  parent=document.querySelector('.card-body'); // 생성된 sell_box 안에 p 넣을거

  let p_ele=document.createElement("p");
  parent.insertBefore(p_ele,null);
  p_ele.innerHTML=bookname;

  p_ele=document.createElement("p");
  parent.insertBefore(p_ele,null);
  p_ele.innerHTML=writer;

  div_ele=document.createElement("div");
  parent.insertBefore(div_ele,null);
  div_ele.setAttribute('class',"price");

  parent=document.querySelector('.price');

  let span_ele=document.createElement("span");
  parent.insertBefore(span_ele,null);
  span_ele.innerHTML=sellprice;

  span_ele=document.createElement("span");
  parent.insertBefore(span_ele,null);
  span_ele.innerHTML=" / ";

  span_ele=document.createElement("span");
  parent.insertBefore(span_ele,null);
  span_ele.innerHTML=originalprice;

  parent=document.querySelector('.card-body');

  div_ele=document.createElement("div");
  parent.insertBefore(div_ele,null);
  div_ele.innerHTML="물건 판매자"

  div_ele=document.createElement("div");
  parent.insertBefore(div_ele,null);
  div_ele.innerHTML="물건 등록일"

  let button_ele=document.createElement("button");
  parent.insertBefore(button_ele,null);
  button_ele.setAttribute('class',"btn btn-primary");
  button_ele.innerHTML="등록";
});