import 'dart:convert';
import 'geo_location.dart';

class Address {
  String street;
  String number;
  String district;
  String zipcode;
  String state;
  String city;
  String complement;
  GeoLocation? geo_location;
  Address({
    required this.street,
    required this.number,
    required this.district,
    required this.zipcode,
    required this.state,
    required this.city,
    required this.complement,
    this.geo_location,
  });

  String getQuery() {
    return street +
        ", " +
        number +
        " - " +
        district +
        ", " +
        city +
        " - " +
        state +
        ", " +
        zipcode +
        ", " +
        "Brasil";
  }

 

  Address copyWith({
    String? street,
    String? number,
    String? district,
    String? zipcode,
    String? state,
    String? city,
    String? complement,
    GeoLocation? geo_location,
  }) {
    return Address(
      street: street ?? this.street,
      number: number ?? this.number,
      district: district ?? this.district,
      zipcode: zipcode ?? this.zipcode,
      state: state ?? this.state,
      city: city ?? this.city,
      complement: complement ?? this.complement,
      geo_location: geo_location ?? this.geo_location,
    );
  }

  Map<String, dynamic> toMap() {
    final result = <String, dynamic>{};
  
    result.addAll({'street': street});
    result.addAll({'number': number});
    result.addAll({'district': district});
    result.addAll({'zipcode': zipcode});
    result.addAll({'state': state});
    result.addAll({'city': city});
    result.addAll({'complement': complement});
    if(geo_location != null){
      result.addAll({'geo_location': geo_location!.toMap()});
    }
  
    return result;
  }

  factory Address.fromMap(Map<String, dynamic> map) {
    return Address(
      street: map['street'] ?? '',
      number: map['number'] ?? '',
      district: map['district'] ?? '',
      zipcode: map['zipcode'] ?? '',
      state: map['state'] ?? '',
      city: map['city'] ?? '',
      complement: map['complement'] ?? '',
      geo_location: map['geo_location'] != null ? GeoLocation.fromMap(map['geo_location']) : null,
    );
  }

  String toJson() => json.encode(toMap());

  factory Address.fromJson(String source) => Address.fromMap(json.decode(source));

  @override
  String toString() {
    return 'Address(street: $street, number: $number, district: $district, zipcode: $zipcode, state: $state, city: $city, complement: $complement, geo_location: $geo_location)';
  }

  @override
  bool operator ==(Object other) {
    if (identical(this, other)) return true;
  
    return other is Address &&
      other.street == street &&
      other.number == number &&
      other.district == district &&
      other.zipcode == zipcode &&
      other.state == state &&
      other.city == city &&
      other.complement == complement &&
      other.geo_location == geo_location;
  }

  @override
  int get hashCode {
    return street.hashCode ^
      number.hashCode ^
      district.hashCode ^
      zipcode.hashCode ^
      state.hashCode ^
      city.hashCode ^
      complement.hashCode ^
      geo_location.hashCode;
  }
}
