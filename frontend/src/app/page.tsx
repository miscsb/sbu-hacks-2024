import Navbar from "@/components/Navbar";
import Sidebar from "@/components/Sidebar";

export default function Home() {
  return (
    <main className="h-screen">
      <Navbar />
      <div className="body pt-16">
        <Sidebar />
         
      </div>
    </main>
  );
}
