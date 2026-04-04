import type { Metadata } from "next"
import { Playfair_Display, Inter, JetBrains_Mono } from "next/font/google"
import "./globals.css"

const playfair = Playfair_Display({
  subsets: ["latin"],
  variable: "--font-serif",
  display: "swap",
})

const inter = Inter({
  subsets: ["latin"],
  variable: "--font-sans",
  display: "swap",
})

const jetbrains = JetBrains_Mono({
  subsets: ["latin"],
  variable: "--font-mono",
  display: "swap",
})

export const metadata: Metadata = {
  title: "Cogito",
  description:
    "The AI that remembers. Your data stays yours.",
  icons: {
    icon: "/logo.svg",
  },
  openGraph: {
    title: "Cogito",
    description:
      "Decentralized, permissionless cognitive AI. Persistent memory, wallet-based identity, self-custodial context.",
    url: "https://cogito.so",
    siteName: "Cogito",
    type: "website",
  },
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html
      lang="en"
      className={`${playfair.variable} ${inter.variable} ${jetbrains.variable}`}
    >
      <body className="font-sans grain-overlay">{children}</body>
    </html>
  )
}
