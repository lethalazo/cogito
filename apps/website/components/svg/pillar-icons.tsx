"use client"

import { motion } from "framer-motion"

interface PillarIconProps {
  type: "memory" | "encryption" | "decentralization"
}

const pathVariants = {
  hidden: { pathLength: 0, opacity: 0 },
  visible: {
    pathLength: 1,
    opacity: 1,
    transition: { duration: 1.5, ease: "easeInOut" },
  },
}

function MemoryIcon() {
  return (
    <svg viewBox="0 0 80 80" fill="none" className="w-20 h-20" aria-hidden="true">
      <motion.g
        variants={{ hidden: {}, visible: {} }}
        initial="hidden"
        whileInView="visible"
        viewport={{ once: true }}
      >
        <circle cx="40" cy="40" r="38" fill="rgba(212, 99, 94, 0.04)" />
        {/* Brain outline */}
        <motion.path
          d="M 40 16 C 28 16 20 24 20 34 C 20 40 23 45 28 48 L 28 62 L 52 62 L 52 48 C 57 45 60 40 60 34 C 60 24 52 16 40 16"
          stroke="currentColor"
          strokeWidth={1.5}
          strokeLinecap="round"
          strokeLinejoin="round"
          variants={pathVariants}
        />
        {/* Neural connections */}
        <motion.path
          d="M 32 62 L 32 56 M 40 62 L 40 56 M 48 62 L 48 56"
          stroke="currentColor"
          strokeWidth={1.2}
          strokeLinecap="round"
          variants={pathVariants}
        />
        {/* Memory nodes */}
        <motion.circle cx="33" cy="32" r="2" fill="currentColor"
          initial={{ opacity: 0, scale: 0 }}
          whileInView={{ opacity: 0.7, scale: 1 }}
          viewport={{ once: true }}
          transition={{ duration: 0.5, delay: 1.2 }}
        />
        <motion.circle cx="47" cy="32" r="2" fill="currentColor"
          initial={{ opacity: 0, scale: 0 }}
          whileInView={{ opacity: 0.7, scale: 1 }}
          viewport={{ once: true }}
          transition={{ duration: 0.5, delay: 1.5 }}
        />
        <motion.circle cx="40" cy="40" r="2" fill="currentColor"
          initial={{ opacity: 0, scale: 0 }}
          whileInView={{ opacity: 0.7, scale: 1 }}
          viewport={{ once: true }}
          transition={{ duration: 0.5, delay: 1.8 }}
        />
        {/* Connecting lines */}
        <motion.path
          d="M 33 32 L 40 40 L 47 32"
          stroke="currentColor"
          strokeWidth={0.8}
          strokeLinecap="round"
          initial={{ pathLength: 0, opacity: 0 }}
          whileInView={{ pathLength: 1, opacity: 0.5 }}
          viewport={{ once: true }}
          transition={{ duration: 1, delay: 1 }}
        />
      </motion.g>
    </svg>
  )
}

function EncryptionIcon() {
  return (
    <svg viewBox="0 0 80 80" fill="none" className="w-20 h-20" aria-hidden="true">
      <motion.g
        variants={{ hidden: {}, visible: {} }}
        initial="hidden"
        whileInView="visible"
        viewport={{ once: true }}
      >
        <circle cx="40" cy="40" r="38" fill="rgba(212, 99, 94, 0.04)" />
        {/* Lock body */}
        <motion.rect
          x="24" y="36" width="32" height="24" rx="3"
          stroke="currentColor"
          strokeWidth={1.5}
          variants={pathVariants}
        />
        {/* Lock shackle */}
        <motion.path
          d="M 30 36 L 30 28 C 30 20 34 16 40 16 C 46 16 50 20 50 28 L 50 36"
          stroke="currentColor"
          strokeWidth={1.5}
          strokeLinecap="round"
          variants={pathVariants}
        />
        {/* Keyhole */}
        <motion.circle cx="40" cy="46" r="3" fill="currentColor"
          initial={{ opacity: 0, scale: 0 }}
          whileInView={{ opacity: 0.7, scale: 1 }}
          viewport={{ once: true }}
          transition={{ duration: 0.5, delay: 1.3 }}
        />
        <motion.path
          d="M 40 49 L 40 54"
          stroke="currentColor"
          strokeWidth={2}
          strokeLinecap="round"
          initial={{ pathLength: 0, opacity: 0 }}
          whileInView={{ pathLength: 1, opacity: 0.7 }}
          viewport={{ once: true }}
          transition={{ duration: 0.5, delay: 1.5 }}
        />
      </motion.g>
    </svg>
  )
}

function DecentralizationIcon() {
  return (
    <svg viewBox="0 0 80 80" fill="none" className="w-20 h-20" aria-hidden="true">
      <motion.g
        variants={{ hidden: {}, visible: {} }}
        initial="hidden"
        whileInView="visible"
        viewport={{ once: true }}
      >
        <circle cx="40" cy="40" r="38" fill="rgba(212, 99, 94, 0.04)" />
        {/* 4 distributed nodes */}
        {[
          { cx: 20, cy: 24 },
          { cx: 60, cy: 24 },
          { cx: 20, cy: 56 },
          { cx: 60, cy: 56 },
        ].map((n, i) => (
          <motion.circle
            key={i}
            cx={n.cx} cy={n.cy} r={6}
            stroke="currentColor"
            strokeWidth={1.2}
            fill="none"
            initial={{ opacity: 0, scale: 0 }}
            whileInView={{ opacity: 1, scale: 1 }}
            viewport={{ once: true }}
            transition={{ duration: 0.4, delay: 0.3 + i * 0.15 }}
          />
        ))}
        {/* Inner dots */}
        {[
          { cx: 20, cy: 24 },
          { cx: 60, cy: 24 },
          { cx: 20, cy: 56 },
          { cx: 60, cy: 56 },
        ].map((n, i) => (
          <motion.circle
            key={`dot-${i}`}
            cx={n.cx} cy={n.cy} r={2}
            fill="currentColor"
            initial={{ opacity: 0 }}
            whileInView={{ opacity: 0.7 }}
            viewport={{ once: true }}
            transition={{ duration: 0.3, delay: 0.5 + i * 0.15 }}
          />
        ))}
        {/* Connection lines - mesh, no central hub */}
        {[
          "M 20 24 L 60 24", "M 20 56 L 60 56",
          "M 20 24 L 20 56", "M 60 24 L 60 56",
          "M 20 24 L 60 56", "M 60 24 L 20 56",
        ].map((d, i) => (
          <motion.path
            key={`line-${i}`}
            d={d}
            stroke="currentColor"
            strokeWidth={0.8}
            strokeDasharray="4 4"
            initial={{ pathLength: 0, opacity: 0 }}
            whileInView={{ pathLength: 1, opacity: 0.3 }}
            viewport={{ once: true }}
            transition={{ duration: 0.8, delay: 0.8 + i * 0.1 }}
          />
        ))}
      </motion.g>
    </svg>
  )
}

export function PillarIcon({ type }: PillarIconProps) {
  const icons = { memory: MemoryIcon, encryption: EncryptionIcon, decentralization: DecentralizationIcon }
  const Icon = icons[type]
  return (
    <div className="flex justify-center my-8 text-accent">
      <Icon />
    </div>
  )
}
