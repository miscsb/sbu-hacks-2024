import { FaArrowUp } from "react-icons/fa";

export default function HomePage() {

  return <div className="homepage w-full h-full flex flex-col items-center justify-center">
    <div className="arrow absolute top-24 right-24">
      <FaArrowUp className="fill-gray-950 w-16 h-16 rotate-45"/>
    </div>
    <h1>Welcome to the Lecture Summarizer.</h1>
    <h3>Create a new summary to get started.</h3>
  </div>

}
