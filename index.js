/* const imagizer=require('imagizer-javascript');
const image_path = './assets/demo2.jpg';
const new_file_name = 'sketch.jpg';

imagizer.OverLay(image_one, image_two, new_file_name, image_one_opacity, image_two_opacity, file_destination).then(img_path => {
    console.log(img_path)
}) */
//FileSaver saveAs();


import { saveAs } from 'file-saver';
function getLink(){
    //var FileSaver = require('file-saver');
    console.log("Hello");
    var link = document.getElementById("text").value;
    console.log(link);
    /*FileSaver.saveAs(link, "demo.jpg"); */
}


