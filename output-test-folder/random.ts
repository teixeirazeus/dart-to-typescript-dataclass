import { Data } from "dataclass";


class Random extends Data {
    street: string;
    date: Date;
    type: boolean;
    stringList: Array<string>;
    stringInt: Array<number>;
    stringDouble: Array<number>;
    distance: number;
    price: Decimal;
    hour: number;
    things: string;
}

export { Random };