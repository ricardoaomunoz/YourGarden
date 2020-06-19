import Validator from 'validator';
import isEmpty from 'lodash/isEmpty';


 export default function validateInput(data) {

     console.log(data.username);
     console.log(data.password);
     data.username = !isEmpty(data.username) ? data.username : '';
     data.password = !isEmpty(data.password) ? data.password : '';
     
     let errors = {};

     if (Validator.isEmpty(data.username)) {
         errors.username = 'This field is required';
     }

     if (Validator.isEmpty(data.password)) {
        errors.password = 'This field is required';
    }

     return {
         errors,
         isValid: isEmpty(errors)
     }
 }