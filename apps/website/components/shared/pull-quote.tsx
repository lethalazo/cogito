"use client"

import { motion } from "framer-motion"

interface PullQuoteProps {
  children: string
}

export function PullQuote({ children }: PullQuoteProps) {
  return (
    <motion.blockquote
      initial={{ opacity: 0, x: -20 }}
      whileInView={{ opacity: 1, x: 0 }}
      viewport={{ once: true, margin: "-40px" }}
      transition={{ duration: 0.7, ease: "easeOut" }}
      className="my-16 md:my-20 pl-6 md:pl-8 border-l-2 border-accent relative max-w-[720px] mx-auto"
    >
      {/* Decorative quote mark */}
      <span className="absolute -left-2 -top-4 font-serif text-5xl text-accent/10 select-none pointer-events-none">
        &ldquo;
      </span>
      <p className="font-serif text-lg sm:text-2xl md:text-3xl leading-snug text-foreground/90 italic">
        &ldquo;{children}&rdquo;
      </p>
    </motion.blockquote>
  )
}
