"use client"

import { motion } from "framer-motion"
import { cn } from "@/lib/utils"

interface SectionWrapperProps {
  children: React.ReactNode
  id?: string
  className?: string
  muted?: boolean
}

export function SectionWrapper({
  children,
  id,
  className,
  muted = false,
}: SectionWrapperProps) {
  return (
    <motion.section
      id={id}
      initial={{ opacity: 0 }}
      whileInView={{ opacity: 1 }}
      viewport={{ once: true, margin: "-100px" }}
      transition={{ duration: 0.8, ease: "easeOut" }}
      className={cn(
        "px-4 sm:px-6 py-20 md:py-32 relative overflow-hidden",
        muted ? "bg-background-subtle" : "bg-background",
        className
      )}
    >
      <div className="max-w-6xl mx-auto">{children}</div>
    </motion.section>
  )
}
