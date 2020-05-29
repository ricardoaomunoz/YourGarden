import React, { Component } from "react";
import {Carousel} from 'react-bootstrap';
import header_img from './images/header_img.jpg'
import imagen_1 from './images/2.jpg'
import imagen_2 from './images/3.jpg'
import imagen_3 from './images/4.jpg'
import imagen_4 from './images/5.jpg'
import imagen_5 from './images/6.jpg'
import imagen_6 from './images/7.jpg'

class CarouselImg extends Component  {
  constructor (props) {
    super(props)
    this.state={
        index: 0,
        handleSelect : (selectedIndex, e) => this.setState({index: selectedIndex}),
        
    }}
    render(){

    return (
      <Carousel activeIndex={this.index} onSelect={this.handleSelect}>
        <Carousel.Item>
          <img width={900} height={400} alt="900x400"
            className="d-block w-100"
            src={header_img}
            alt="First slide"
          />
          <Carousel.Caption>
            <h3>First slide label</h3>
            <p>Nulla vitae elit libero, a pharetra augue mollis interdum.</p>
          </Carousel.Caption>
        </Carousel.Item>
        <Carousel.Item>
          <img width={900} height={400} alt="900x400"
            className="d-block w-100"
            src={imagen_2}
            alt="Second slide"
          />
  
          <Carousel.Caption>
            <h3>Second slide label</h3>
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
          </Carousel.Caption>
        </Carousel.Item>
        <Carousel.Item>
          <img width={900} height={400} alt="900x400"
            className="d-block w-100"
            src={imagen_1}
            alt="Third slide"
          />
  
          <Carousel.Caption>
            <h3>Third slide label</h3>
            <p>
              Praesent commodo cursus magna, vel scelerisque nisl consectetur.
            </p>
          </Carousel.Caption>
        </Carousel.Item>
        <Carousel.Item>
          <img width={900} height={400} alt="900x400"
            className="d-block w-100"
            src={imagen_3}
            alt="First slide"
          />
          <Carousel.Caption>
            <h3>First slide label</h3>
            <p>Nulla vitae elit libero, a pharetra augue mollis interdum.</p>
          </Carousel.Caption>
        </Carousel.Item>
        <Carousel.Item>
          <img width={900} height={400} alt="900x400"
            className="d-block w-100"
            src={imagen_4}
            alt="First slide"
          />
          <Carousel.Caption>
            <h3>First slide label</h3>
            <p>Nulla vitae elit libero, a pharetra augue mollis interdum.</p>
          </Carousel.Caption>
        </Carousel.Item>
        <Carousel.Item>
          <img width={900} height={400} alt="900x400"
            className="d-block w-100"
            src={imagen_5}
            alt="First slide"
          />
          <Carousel.Caption>
            <h3>First slide label</h3>
            <p>Nulla vitae elit libero, a pharetra augue mollis interdum.</p>
          </Carousel.Caption>
        </Carousel.Item>
        <Carousel.Item>
          <img width={900} height={400} alt="900x400"
            className="d-block w-100"
            src={imagen_6}
            alt="First slide"
          />
          <Carousel.Caption>
            <h3>First slide label</h3>
            <p>Nulla vitae elit libero, a pharetra augue mollis interdum.</p>
          </Carousel.Caption>
        </Carousel.Item>
        
      </Carousel>
    );
  }
}
export default CarouselImg