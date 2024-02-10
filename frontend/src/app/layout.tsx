import type { Metadata } from "next";
import { Inter } from "next/font/google";
import "./globals.css";

import Navbar from "@/components/Navbar";
import Sidebar from "@/components/Sidebar";

const inter = Inter({ subsets: ["latin"] });

export const metadata: Metadata = {
  title: "Create Next App",
  description: "Generated by create next app",
};

type Props = Readonly<{
  children: React.ReactNode;
}>;

export default function RootLayout({children}: Props) {

  return (
    <html lang="en">
      <body className={inter.className}>

        <main className="h-screen flex flex-col">

          <Navbar />

          <div className="flex flex-row flex-grow h-full pt-16 overflow-auto">
            <Sidebar />
            <div className="notes flex-grow bg-gray-100 p-8 overflow-auto">
              {children}
            </div>
          </div>

        </main>

      </body>
    </html>
  );
}
