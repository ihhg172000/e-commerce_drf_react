import "./ShoppingBag.css";
import { ReactComponent as ShoppingBagIcon } from "../Assets/shopping_bag.svg";

export const ShoppingBag = () => {
  return (
    <div className="shopping-bag">
      <span></span>
      <ShoppingBagIcon />
    </div>
  );
};
