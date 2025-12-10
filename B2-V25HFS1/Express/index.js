// let express=require("express")
// let app=express()
// app.listen(5000,()=>{
//     console.log("server started at http://localhost:5000")
// })
// app.get("/",(req,res)=>{
//     res.send("request on / path")
// })

// app.get("/about",(req,res)=>{
//     res.send("request on /about path")
// })

// app.get("/login",(req,res)=>{
//     res.send("request on /login path")
// })
let express=require("express")
let app=express()
app.listen(5000)
app.use(express.json())
app.get("/",(req,res)=>{
    console.log(req.url)
    res.send("respond received on /path")
})
app.get("/search",(req,res)=>{
    res.send(" Basic search")
})
app.get("/search/:id",(req,res)=>{
    console.log(req.params.id)
    res.send("This is your data")
})
app.get("/search/:id/:data",(req,res)=>{
    console.log(req.params.id,req.params.data)
    res.send("Advanced search")
})
app.post("/add",(req,res)=>{
    console.log(req.body)
    res.send("Data received")
})