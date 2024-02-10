import Markdown from "@/components/Markdown";
import Navbar from "@/components/Navbar";
import Sidebar from "@/components/Sidebar";

// for testing
import fetchData from "@/lib/fetchData";

export default async function Home() {

  const markdown = `# Hello World
  ## Hello World
  ### Hello world
  This is a test of the markdown component.
  ~~~javascript
  console.log('Hello World');
  ~~~
  `;

  const res = await fetchData('http://127.0.0.1:5000/sessions');
  const data = await res.json();

  return (
    <main className="h-screen flex flex-col">
      <Navbar />
      <div className="flex flex-row flex-grow h-full pt-16 overflow-auto">
        <Sidebar />
        <div className="notes flex-grow bg-gray-100 p-8 overflow-auto">
          <Markdown markdown={markdown} />
          <div className="data">
            {data.answer}
          </div>
        </div>
      </div>
    </main>
  );
}
