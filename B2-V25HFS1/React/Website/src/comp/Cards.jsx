import axios from "axios";
import { useEffect, useState } from "react";
import Product from "./Product";

const Cards = () => {
  let [data, setData] = useState([]);
  useEffect(() => {
    axios.get("https://fakestoreapi.com/products").then((res) => {
      setData(res.data);
    });
  }, []);
  return (
    <div className="prodcon">
      <h1>Products List</h1>
      <div className="prodmapgrid">
        {data.map((obj) => (
          <Product obj={obj} />
        ))}
      </div>
    </div>
  );
};

export default Cards;