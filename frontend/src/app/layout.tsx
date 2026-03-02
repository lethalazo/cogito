import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "Cogito",
  description: "Cognitive AI agent framework",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
