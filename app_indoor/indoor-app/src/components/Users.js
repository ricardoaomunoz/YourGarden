import React from 'react'
import PropTypes from 'prop-types'

function Users (props) {
  const {name, id} = props.name
  console.log("llego al component users\n");
  console.log(id);
  console.log(name);
  return <p><strong>{id}: </strong>{name}</p>
}

// Users.PropTypes = {
//   users: PropTypes.shape({
//     id: PropTypes.string,
//     name: PropTypes.string,
//     // timestamp: PropTypes.instanceOf(Date)
//   })
// }

export default Users;