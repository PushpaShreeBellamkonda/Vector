import { useEffect, useState } from "react"

 let arr=[{"img":"https://t3.ftcdn.net/jpg/04/01/36/86/360_F_401368641_nEdHMBlrlmyW09cBtm4lvb83EtN7Gx5t.jpg","title":"Heading Text-1","data":"react components-1"},
    {"img":"https://t4.ftcdn.net/jpg/05/49/04/05/360_F_549040524_csZXoBJYqcNb2jAEkhwBSDs88cNSgt98.jpg","title":"Heading Text-2","data":"react components-2"},
    {"img":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ3KJVe0Z0PR-_LEGF-pxO683y7OPvTpIit-A&s","title":"Heading Text-3","data":"react components-3"},
    {"img":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT2ge2-Z91gjg9OZO7UEKVn4sx0Hl_2coqd7Q&s","title":"Heading Text-4","data":"react components-4"},
    {"img":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRSwWSvGQZPnOm_zcqfcN0mUBC5ltQdrlI4og&s","title":"Heading Text-5","data":"react components-5"},
    {"img":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRX71G28V9N4PSbCPA0kZ5dTOABYPW9IozX_Q&s","title":"Heading Text-6","data":"react components-6"},
    {"img":"https://t4.ftcdn.net/jpg/04/52/38/65/360_F_452386512_vkOwz3zZ0dLWvjZku0MANPowNs32W7hm.jpg","title":"Heading Text-7","data":"react components-7"},
    {"img":"https://media.istockphoto.com/id/1156285298/vector/futuristic-education-technology-page-for-smartphone-application-isometric-banner-for-online.jpg?s=612x612&w=0&k=20&c=kxDHdQ59S6Q_3BLAfs8OPWVxZa9Bevu1SZPxn7LEoTw=","title":"Heading Text-8","data":"react components-8"}]

const Cour = () => {
   let [i,setI]=useState(0)

   let fwd=()=>{
    setI((i)=>(i+1)%arr.length)
   }
   
   let bkw=()=>{
    if(i==0)
    {
        setI(arr.length-1)
    }
    else{
        setI(i-1)
    }
   }
   useEffect(()=>{
    let iid=setInterval(fwd,2000)
    return ()=>{
        clearInterval(iid)
    }
   },[])
  return (
    <div className="bnr">
        <img src={arr[i].img}/>
        <i class="fa-solid fa-less-than" onClick={bkw}></i>
        <i class="fa-solid fa-greater-than" onClick={fwd}></i>
        <div className="circles">
            {
                arr.map((img,ind)=>{
                    return <i class={i==ind?"fa-solid fa-circle":"fa-regular fa-circle"} onClick={()=>setI(ind)}></i>
                })
            }
        </div>

        <div className="content">
            <h1>{arr[i].title}</h1>
            <p>{arr[i].data}</p>
        </div>
    </div>
  )
}

export default Cour