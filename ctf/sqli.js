/* 
@author: konchan
@practice build lab
 __                       .__                                         .__  .__ 
|  | ______   ____   ____ |  |__ _____    ____             ___________|  | |__|
|  |/ /  _ \ /    \_/ ___\|  |  \\__  \  /    \   ______  /  ___/ ____/  | |  |
|    <  <_> )   |  \  \___|   Y  \/ __ \|   |  \ /_____/  \___ < <_|  |  |_|  |
|__|_ \____/|___|  /\___  >___|  (____  /___|  /         /____  >__   |____/__|
     \/          \/     \/     \/     \/     \/               \/   |__|        

*/
const express = require('express');
const fs = require('fs')
const bodyParser = require('body-parser');
const mysql      = require('mysql');


const FLAG=fs.readFileSync('./flag.txt','utf-8')
const app=express()
app.use(express.json())

const db = mysql.createConnection({
    host     : 'localhost',
    user     : 'root',
    password : 'root',
    database : 'democtf'
  });
  
db.connect(function(err) {
  if (err) throw err;
  console.log('connect ...');
})


// db.query('create database democtf;')
// db.query('CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))')
// db.query(`insert into customers (name,address) values ('konchan','China'),('spcyio','Japan'),('hacker','VietName'),('Trciker','${FLAG}')`)
app.get('/',async (req,res)=>{
    res.send('Do you wanna hack me. Try /heaths')
})
app.post('/heaths',async (req,res)=>{
        if (req.body.address){
        const sql='select * from customers where address="'+req.body.address+'"'
        db.query(sql,(err,results,fields)=>{
            if (err) throw err;
            res.send(results)
        });
    }
});
app.listen(1234,()=>{
    console.log(1234)
})
