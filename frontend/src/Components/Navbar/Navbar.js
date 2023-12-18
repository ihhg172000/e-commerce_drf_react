import "./Navbar.css";
import { ShoppingBag } from "../ShoppingBag/ShopingBag";

export const Navbar = () => {
  return (
    <div className="navbar">
      <h1>Eg4Tech</h1>
      <div>
        <ShoppingBag />
        <a href="#">Login</a>
      </div>
    </div>
  );
};
