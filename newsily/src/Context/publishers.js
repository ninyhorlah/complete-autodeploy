import React from 'react';
import { config } from '../Components/Constantss'
import axios from 'axios'
import { Link } from 'react-router-dom';
import Button from 'react-bootstrap/Button'

var URL = config.url.API_URL

const Publishers = (props) => {

    const DisplayPublishers = (props) => {
        
        const {publishers} = props

        const handleSubscribe = (id, description) => {
            let token = JSON.parse(localStorage.getItem('currentUser')).token

            var data = {
                "subscription" : id,
                "description": "My subscriptions"
            }

            var headers = {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${token}`
            }

            axios.post(`${URL}/subscriptions/subscribe/`, data, {
                headers : headers
            })
            .then(function(response) {
                console.log(response)
            })
            window.location.reload();
        }

        if (publishers.length > 0) {
            return (
                publishers.map(({logo, id, description}, index) => {
                    return (
                        <div className="col-sm exploreee">
                            <Button onClick={() => handleSubscribe(id, description)} className="btn-explore-img">
                                <img src={logo} alt="test" width="180px" height="180px"/>
                            </Button>
                        </div>
                    )
                })
            )
        } else {
            return (
                <div>
                    No publishers
                </div>
            )
        }

    }

    return (
        <div className="explore-section">
            <div className="row">
                <div className="col-sm-4">
                    
                </div>
                <div className="col-sm-8">
                    <div className="row badge-section-body">
                        <div className="col-sm-3">
                            Category
                        </div>
                        <div className="col-sm-8">
                            <span className="badge bg-info text-dark badge-body general-badge">GENERAL</span>{' '}
                            <span className="badge bg-primary text-dark badge-body">SPORTS</span>{' '}
                            <span className="badge bg-danger text-dark badge-body">FINANCE</span>{' '}
                            {/* <span className="badge bg-success text-dark badge-body">ENTERTAINMENT</span>{' '} */}
                        </div>
                    </div>
                </div>
            </div>

            <div className="row explore-div">
                <div className="col-sm-4">
                    <h1 className="explore">Select your trusted news</h1>
                    <div className="explore-btn">
                        <Link href="#" className="explore-btn-btn">EXPLORE MORE</Link>
                    </div>
                </div>
                <div className="col-sm-8">
                    <div className="row row-cols-3">
                        {DisplayPublishers(props)}
                    </div>
                </div>
            </div>
        </div>
    )
}


export default Publishers