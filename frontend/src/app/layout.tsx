import "./globals.css";
import { Inter } from "next/font/google";
import type { Metadata } from "next";
import { ReactNode } from "react";
import Providers from "./providers";

const inter = Inter({ subsets: ["latin"] });

export const metadata: Metadata = {
  title: "IoT Dashboard",
  description: "Track your IoT devices",
};

export default function RootLayout({ children }: { children: ReactNode }) {
  return (
    <html lang="en">
      <body className={inter.className}>
        <Providers>
          {children}
        </Providers>
      </body>
    </html>
  );
}
