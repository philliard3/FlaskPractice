var rect = [50, 20, 80, 80];
var frames = [[50, 20, 80, 80], [20, 30, 80, 90], [50, 20, 60, 80], [0, 20, 80, 80]];
var cur_frame = 0;
function redraw(){
    //console.log("I'm in the function");
    //console.log("The elements are");
    var polygon = "polygon("+(rect[0])+"px "+(rect[1])+"px, "+(rect[2])+"px "+rect[1]+"px, "+(rect[2])+"px "+(rect[3])+"px, "+(rect[0])+"px "+(rect[3])+"px);";
    //console.log("before: "+(document.getElementById("clippable").getAttribute("clip-path")));
    document.getElementById("clippable").setAttribute("style", "clip-path:"+polygon);
}

function redraw_left(){
    rect[0] -= 5;
    if(rect[0]<0){
        rect[2] = rect[2] -5 - rect[0];
        rect[0]=0;
    }else{
        rect[2] -= 5;
    }
    redraw();
}


function redraw_right(){

    rect[2] +=5;
    if(rect[2]>100){
        rect[0] = rect[0] + 5 - (rect[2]-100);
        rect[2]=100;
    }else{
        rect[0] += 5;
    }
    redraw();
}

function redraw_square(){
    rect[2] = rect[0]+30;
    rect[3] = rect[1]+30;
    redraw();
}

function next_frame(){
    cur_frame+=1;
    if(cur_frame>=frames.length){
        cur_frame=0;
        rect = frames[0];
    }else{
        rect = frames[cur_frame];
    }
    redraw();
}

function clear(){
    console.log("attempting to clear");
}
