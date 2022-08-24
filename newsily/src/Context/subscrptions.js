import React from 'react';
import { Button } from 'react-bootstrap';


const GetUserSubscription = (props) => {

    const displaySubscriptions = (props) => {

        const {subscriptions} = props;

        // const badgecolor = () => {
        //     const blue = "" 
        // }

        if (subscriptions.length > 0) {
            return (
                subscriptions.map((subscription, index) => {
                    return (         
                        <div className="col" style={{ paddingTop: '20px' }}>
                            <div className="background-img" style={{ width: 'auto', padding: '10px'}}>
                                <img src={subscription.subscription_details.background_image} 
                                    alt={subscription.subscription_details.name} 
                                    width = "100%"
                                    height = "auto"
                                />

                                <div className="col-xxl-8 px-4">
                                    <div className="row flex-lg-row-reverse align-items-center">
                                        <div className="col-lg-6 d-grid gap-7 d-md-flex btnContainer">
                                            {/* <Button className="lightBtn">MANAGE</Button>{' '} */}
                                            <Button
                                                href={subscription.subscription_details.url} 
                                                className="darkBtn"
                                                variant="dark">READ
                                            </Button>{' '}
                                        </div>
                                        
                                        <div className="col-10 col-sm-8 col-lg-6 todayBtn">
                                                <img src={subscription.subscription_details.logo} 
                                                    alt={subscription.subscription_details.name}/>
                                        </div>
                                    </div>
                                </div>

                                <div className="card-body">
                                    <h5 className="card-title">{subscription.subscription_details.name}</h5>
                                    <p className="card-text" style={{ fontSize: '14px' }}>
                                        {subscription.subscription_details.description}
                                    </p>
                                    {/* <span 
                                        className="badge text-dark text-uppercase"
                                    >
                                            {subscription.subscription_details.catergory}
                                    </span> */}
                                </div>
                            </div>
                        </div>
                )
                })
            )
        } else {
            return (
                    <h3 className="no-subscriptions">You have no subscriptions</h3>
            )
        }
    }

    return (
        <div className="section-one">
            <h1 className="text-center">
                Your Subscriptions
            </h1>  
            <div className="row row-cols-1 row-cols-sm-2 row-cols-md-3 g-3 card-section">
                {displaySubscriptions(props)}
            </div>
        </div>
    )
}

export default GetUserSubscription