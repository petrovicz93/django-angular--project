import {Product} from "./product";

export class Variation {
  id?: number;
  title?: string;
  product: Product;
  variation?: string;
  price?: number;
  sku?: string;
  select: Boolean = false;
  image?: string;
  amount?: number = 1;
}
