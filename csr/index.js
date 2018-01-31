import { h, render, Component } from 'preact';
import axios from 'axios'

class List extends Component {
    constructor() {
        super();
        this.state.ads = []
    }

    componentDidMount() {
        let ads = []
        axios.get('/api/ads').then(res => {
            this.setState({
                ads: res.data
            })
            ads = res.data
        }).then(() => {
            return axios.get('/api/ads')
        }).then(res => {
            this.setState({
                ads: res.data.concat(ads)
            })
        })
    }

    render(props, state) {
        return  <div>
                    {state.ads.map(ad => (
                        <div>
                            <h2>{ad.title}</h2>
                            <p>{ad.desc}</p>
                            <img src={ad.image} />
                        </div>
                    ))}
                </div>
    }
}

render(<List />, document.body);