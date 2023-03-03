var express= require('express');
var app=express();
app.get('/',function(req,res){
res.send("hello world");
});
app.listen(1234,"222.111.2.1")
