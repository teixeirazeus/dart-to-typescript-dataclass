import { Data } from "dataclass";


class Address extends Data { 
    street: string;
    number: string;
    district: string;
    zipcode: string;
    state: string;
    city: string;
    complement: string;
    geo_location: GeoLocation;
} 

export { Address };