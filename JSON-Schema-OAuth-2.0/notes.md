### JSON Schema and OAuth 2.0

### JSON Schema Validation 
JSON data ka structure aur type expected format ko check karte h ki sahi hai ya nahi. 
Isse data validation easy ho jaata hai before use in API ya database.

### JSON
ek lightweight data format hai 
jo data ko store aur transfer karta h
Yeh data ko key-value pairs ke form mein represent karta hai, 
jaise ek dictionary.

### JSON Schema
JSON data ka structure define karta hai — jaise kis type ka data (string, number, object, etc.) hona chahiye.
Yeh developers ko help karta hai data validate karne aur ensure karne ke liye ki JSON format sahi hai.

### JSON Schema me hum check kar sakte hain ki 
data ka structure sahi hai ya nahi — jaise keys, data types, aur required fields.
Yeh ensure karta hai ki JSON data valid aur expected format me ho.

### How to do it in Postman : -
 1. Copy the response to these sites
 // Create the Schema using jsonschema.net
 // another tool - https://easy-json-schema.github.io/
 // https://www.liquid-technologies.com/online-json-to-schema-converter"
 2.  create a variable like this 
var schema = {); put into it
 3. Use Tiny validate to verify with reponse data.
 pm.test('JSON Schema', function() {
  var jsonData = pm.response.json();
  pm.expect(tv4.validate(jsonData, schema)).to.be.true;
 });

### JSON Schema :
 https://www.jsonschemavalidator.net/
 https://www.jsonschemavalidator.net/s/hG6wNqk4
 https://ajv.js.org/keywords.html
 https://www.jsonschema.net/app/schemas/0

### How to do in REST ASSURED?
 <dependency>  
    <groupId>io.rest-assured</groupId>  
    <artifactId>json-schema-validator</artifactId>
    <version>4.3.1</version>
 </dependency>
 Adding maven dependency of json-schema-validator
 import io.restassured.module.jsv.JsonSchemaValidator;
 JsonSchemaValidator.matchesJsonSchemaInClasspath("AuthJsonSchema.json")

### OAuth 2.0
ek authorization protocol hai jo user ke data ko secure tarike se share karne deta hai 
bina password diye.
Ye access token ke through third-party apps ko limited access deta hai user ke account par.

