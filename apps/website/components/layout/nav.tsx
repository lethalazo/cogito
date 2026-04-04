"use client"

import { useCallback, useEffect, useState } from "react"
import { motion } from "framer-motion"
import { Logo } from "@/components/logo"
import { cn } from "@/lib/utils"

const NAV_LINKS = [
  { href: "problem", label: "Problem" },
  { href: "solution", label: "Solution" },
  { href: "how-it-works", label: "How It Works" },
  { href: "roadmap", label: "Roadmap" },
]

export function Nav() {
  const [scrolled, setScrolled] = useState(false)

  useEffect(() => {
    const onScroll = () => setScrolled(window.scrollY > 50)
    window.addEventListener("scroll", onScroll, { passive: true })
    return () => window.removeEventListener("scroll", onScroll)
  }, [])

  const handleNavClick = useCallback(
    (e: React.MouseEvent<HTMLAnchorElement>, id: string) => {
      const el = document.getElementById(id)
      if (el) {
        e.preventDefault()
        el.scrollIntoView({ behavior: "smooth" })
      }
    },
    []
  )

  return (
    <motion.nav
      initial={{ y: -20, opacity: 0 }}
      animate={{ y: 0, opacity: 1 }}
      transition={{ duration: 0.6, delay: 0.5 }}
      className={cn(
        "fixed top-0 left-0 right-0 z-50 transition-all duration-500",
        scrolled
          ? "bg-background/90 backdrop-blur-md border-b border-border/50 shadow-[0_4px_30px_rgba(0,0,0,0.06)]"
          : "bg-transparent"
      )}
    >
      <div className="max-w-6xl mx-auto px-6 h-16 flex items-center justify-between">
        <a
          href="/"
          className="flex items-center gap-2.5 hover:opacity-80 transition-opacity duration-300"
        >
          <Logo size={32} />
          <span className="font-serif text-lg tracking-wide text-foreground">
            Cogito
          </span>
        </a>
        <div className="hidden md:flex items-center gap-8">
          {NAV_LINKS.map((link, i) => (
            <motion.a
              key={link.href}
              href={`/#${link.href}`}
              onClick={(e) => handleNavClick(e, link.href)}
              initial={{ opacity: 0, y: -10 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.4, delay: 0.7 + i * 0.1 }}
              className="font-mono text-xs tracking-[0.15em] uppercase text-muted-foreground hover:text-accent transition-colors duration-300 relative group"
            >
              {link.label}
              <span className="absolute -bottom-1 left-0 w-0 h-px bg-accent group-hover:w-full transition-all duration-300" />
            </motion.a>
          ))}
        </div>
      </div>
    </motion.nav>
  )
}
