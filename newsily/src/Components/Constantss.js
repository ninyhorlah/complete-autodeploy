const prod = {
    url : {
        API_URL : 'https://newsily.herokuapp.com'
    }
};


const dev = {
    url : {
        API_URL : 'http://localhost:8000'
    }
}

export const config = process.env.NODE_ENV === "development" ? dev : prod;