import Rating from "@mui/material/Rating";
const Product = (props) => {
  let { title, image, description, price, rating } = props.obj;
  return (
    <div className="prodcard">
      <img src={image} />
      <div className="details">
        <p>{title}</p>
        <p>{description}</p>
        <p>${price}/-</p>
        <Rating
          name="half-rating-read"
          defaultValue={rating.rate}
          precision={0.5}
          readOnly
        />
      </div>6
    </div>
  );
};

export default Product;