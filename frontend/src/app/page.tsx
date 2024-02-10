import Markdown from "@/components/Markdown";
import Navbar from "@/components/Navbar";
import Sidebar from "@/components/Sidebar";

// for testing
import fetchData from "@/lib/fetchData";

export default async function Home() {

  const markdown = `# Hello World
  This is a test of the markdown component.
  ~~~javascript
  console.log('Hello World');
  ~~~
  `;

  const res = await fetchData('https://jsonplaceholder.typicode.com/posts');
  const data = await res.json();

  return (
    <main className="h-screen flex flex-col">
      <Navbar />
      <div className="flex flex-row flex-grow pt-16">
        <Sidebar />
        <div className="notes flex-grow bg-[#888] p-8">
          <Markdown markdown={markdown} />
          <div className="data">
            {data.answer}
          </div>
        </div>
      </div>
    </main>
  );
}
