import axios from "axios"
import {
  NEW_CONNECTOR_JHFUHTG_NAME,
  NEW_CONNECTOR_JHFUHTG_SECRET
} from "react-native-dotenv"
const newConnectorjhfuhtg = axios.create({
  baseURL: "https://app.crowdbotics.com/dashboard/app/20130/storyboard/99273/",
  params: { private_key: NEW_CONNECTOR_JHFUHTG_NAME },
  headers: { Accept: "application/json", "Content-Type": "application/json" }
})
export const apiService = {}
